import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_pdf(filename="Juie_Deshmukh_Resume.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )
    
    styles = getSampleStyleSheet()
    
    name_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#111827'),
        spaceAfter=4
    )
    
    contact_style = ParagraphStyle(
        'ContactLine',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#374151'),
        spaceAfter=10
    )
    
    section_head_style = ParagraphStyle(
        'SectionHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=8,
        spaceAfter=3,
        borderPadding=(0, 0, 2, 0),
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=4
    )
    
    company_style = ParagraphStyle(
        'CompanyHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#111827')
    )
    
    role_style = ParagraphStyle(
        'RoleTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=11.5,
        textColor=colors.HexColor('#374151')
    )
    
    date_style = ParagraphStyle(
        'DateHead',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#374151')
    )
    
    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=11.8,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#1f2937'),
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    story = []

    # Header
    story.append(Paragraph("JUIE DESHMUKH", name_style))
    story.append(Paragraph(
        "juiedeshmukh86@gmail.com &nbsp;|&nbsp; +91-7219741772 &nbsp;|&nbsp; Pune, India &nbsp;|&nbsp; LinkedIn &nbsp;|&nbsp; Portfolio",
        contact_style
    ))
    
    def add_section_divider(title):
        p = Paragraph(title.upper(), section_head_style)
        t = Table([[p]], colWidths=[540])
        t.setStyle(TableStyle([
            ('LINEBELOW', (0,0), (-1,-1), 1, colors.HexColor('#334155')),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    # Professional Summary
    story.append(add_section_divider("Professional Summary"))
    story.append(Spacer(1, 4))
    summary_text = (
        "RPA Consultant and QA professional with <b>5 years and 11 months</b> of experience in RPA validation, manual testing, "
        "functional testing, regression testing, and User Acceptance Testing (UAT) across healthcare and enterprise applications. "
        "Experienced in <b>UiPath, CA PAM, Epic, and Tapestry</b>, with a proven track record of executing <b>2,300+ test cases</b>, "
        "identifying <b>650+ defects</b>, and validating <b>120+ RPA workflows and bots</b>. Skilled in end-to-end RPA/RDA validation, "
        "test suite management, defect lifecycle management, REST API testing, SQL backend validation, Agile delivery, project-level "
        "coordination, and client interaction. Basic exposure to Selenium WebDriver and TestNG for UI automation testing."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 3))

    # Professional Experience
    story.append(add_section_divider("Professional Experience"))
    story.append(Spacer(1, 4))
    
    # Kaiser Permanente
    kp_table = Table([
        [Paragraph("<b>Kaiser Permanente</b>", company_style), Paragraph("Aug 2025 – Present", date_style)],
        [Paragraph("RPA Consultant", role_style), Paragraph("", date_style)]
    ], colWidths=[380, 160])
    kp_table.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(kp_table)
    story.append(Spacer(1, 2))
    
    kp_bullets = [
        "Perform RPA testing and validation for enterprise healthcare applications, including Epic and Tapestry.",
        "Execute functional testing, regression testing, and UAT (800+ test cases) for RPA workflows developed using UiPath and CA PAM.",
        "Validate end-to-end RPA workflows and bot execution, verifying business rules, data accuracy, exception handling, and expected outcomes.",
        "Design, organize, maintain, and execute test cases, test scenarios, and test suites against business and functional requirements.",
        "Manage the defect lifecycle by logging, tracking, retesting, and verifying defects in JIRA.",
        "Collaborate with RPA developers, business analysts, and stakeholders during Agile/Scrum ceremonies and defect triage meetings."
    ]
    for b in kp_bullets:
        story.append(Paragraph(f"&bull;&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 5))

    # Cognizant
    cts_table = Table([
        [Paragraph("<b>Cognizant Technology Solutions, Pune</b>", company_style), Paragraph("Nov 2020 – Jul 2025", date_style)],
        [Paragraph("Programmer Analyst / QA Analyst", role_style), Paragraph("", date_style)]
    ], colWidths=[380, 160])
    cts_table.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(cts_table)
    story.append(Spacer(1, 2))

    cts_bullets = [
        "Executed 1,500+ test cases across diverse testing activities and identified 500+ defects through systematic test execution and defect reporting.",
        "Led end-to-end validation of RPA and RDA bots, verifying workflow execution, business rules, data accuracy, and expected results.",
        "Validated 100+ RPA workflows and bots through functional testing, regression testing, and end-to-end testing cycles.",
        "Took ownership of project-level testing activities, supporting test planning, execution, defect triage, and test status communication.",
        "Supported on-site project activities and client interactions, coordinating with stakeholders to communicate testing progress and quality issues.",
        "Performed manual, functional, and regression testing for web and enterprise applications.",
        "Supported RPA testing initiatives using UiPath and gained exposure to Selenium WebDriver and TestNG for UI test automation and test script execution.",
        "Conducted REST API testing using Postman and SoapUI, with backend data validation using SQL.",
        "Prepared and maintained test cases, test suites, test execution reports, defect logs, and test documentation.",
        "Participated in sprint planning, daily stand-ups, sprint reviews, and defect triage within Agile teams."
    ]
    for b in cts_bullets:
        story.append(Paragraph(f"&bull;&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 3))

    # Technical Skills
    story.append(add_section_divider("Technical Skills"))
    story.append(Spacer(1, 4))
    
    skills = [
        ("RPA and RDA", "UiPath, UiPath Orchestrator, CA PAM, RPA Bot Validation, RDA Bot Validation, End-to-End Workflow Validation"),
        ("Testing", "Manual Testing, Functional Testing, Regression Testing, UAT, End-to-End Testing, Test Case Design, Test Suite Management, Test Execution"),
        ("Test Management", "Test Planning Support, Test Documentation, Defect Lifecycle Management, Defect Tracking, Test Execution Reporting, JIRA, HP ALM"),
        ("Automation", "Basic Selenium WebDriver, TestNG Fundamentals, Java Fundamentals"),
        ("API and Database", "REST API Testing, Postman, SoapUI, SQL, Backend Data Validation"),
        ("Domain and Methodology", "Healthcare Applications, Epic, Tapestry, Agile, Scrum, Client Coordination, Project-Level Testing Ownership")
    ]
    for cat, items in skills:
        p_skill = Paragraph(f"<b>{cat}:</b> {items}", bullet_style)
        story.append(p_skill)
    story.append(Spacer(1, 3))

    # Relevant Projects
    story.append(add_section_divider("Relevant Projects"))
    story.append(Spacer(1, 4))
    
    proj1_table = Table([
        [Paragraph("<b>Healthcare RPA Testing Project</b>", company_style), Paragraph("UiPath, Orchestrator, Excel, SQL", date_style)]
    ], colWidths=[360, 180])
    proj1_table.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(proj1_table)
    story.append(Paragraph("Validated healthcare operational workflows, bot logic, exception handling, data accuracy, and end-to-end execution through functional and regression testing.", body_style))
    story.append(Spacer(1, 2))

    proj2_table = Table([
        [Paragraph("<b>Selenium UI Testing Exposure</b>", company_style), Paragraph("Selenium WebDriver, TestNG, Java", date_style)]
    ], colWidths=[360, 180])
    proj2_table.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(proj2_table)
    story.append(Paragraph("Gained exposure to UI automation concepts, test script execution, and regression testing using Selenium WebDriver and TestNG.", body_style))
    story.append(Spacer(1, 3))

    # Education
    story.append(add_section_divider("Education"))
    story.append(Spacer(1, 4))
    
    edu_table1 = Table([
        [Paragraph("<b>Master of Business Administration (MBA)</b> - Business Analytics & Operations", company_style), Paragraph("Oct 2022 – Jul 2024", date_style)],
        [Paragraph("ASM Group of Institutes &nbsp;|&nbsp; Grade: CGPA 7", role_style), Paragraph("", date_style)]
    ], colWidths=[400, 140])
    edu_table1.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table1)
    story.append(Spacer(1, 2))

    edu_table2 = Table([
        [Paragraph("<b>Bachelor of Science (B.Sc.) in Mathematics</b>", company_style), Paragraph("Graduated: 2020", date_style)],
        [Paragraph("Shri Shivaji Science College, Amravati", role_style), Paragraph("", date_style)]
    ], colWidths=[400, 140])
    edu_table2.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table2)

    doc.build(story)
    print("Resume PDF successfully built:", filename)

if __name__ == "__main__":
    build_pdf("Juie_Deshmukh_Resume.pdf")
    build_pdf("repo/Juie_Deshmukh_Resume.pdf")
